use hound;
use rustfft::num_complex::Complex;
use rustfft::FftPlanner;

use std::io::Cursor;

const WINDOW_SIZE: usize = 1024;
const HOP_SIZE: usize = 512;

pub fn read_audio_file(wav_data: &[u8]) -> Result<Vec<f32>, Box<dyn std::error::Error>> {
    let cursor = Cursor::new(wav_data);
    let mut reader = hound::WavReader::new(cursor)?;
    reader.spec();
    let samples: Vec<f32> = reader
        .samples::<i16>()
        .map(|s| s.unwrap() as f32 / i16::MAX as f32)
        .collect();
    Ok(samples)
}

pub fn generate_spectrogram(audio_data: &[f32]) -> Vec<Vec<f32>> {
    let mut planner = FftPlanner::new();
    let fft = planner.plan_fft_forward(WINDOW_SIZE);
    let mut spectrogram = Vec::new();
    for start in (0..audio_data.len() - WINDOW_SIZE).step_by(HOP_SIZE) {
        let window = &audio_data[start..start + WINDOW_SIZE];
        let mut buffer: Vec<Complex<f32>> = window.iter().map(|&x| Complex::new(x, 0.0)).collect();
        fft.process(&mut buffer);

        let magnitudes: Vec<f32> = buffer.iter().map(|c| c.norm()).collect();
        spectrogram.push(magnitudes);
    }
    spectrogram
}

// pub fn get_spectrogram(input_audio: i32) -> Vec<u8> {
//     // Load image and convert to grayscale
//     let input_image = input_image.to_luma8();

//     // Detect edges using Canny algorithm
//     let edges = canny(&input_image, 50.0, 100.0);

//     // Detect lines using Hough transform
//     let options = LineDetectionOptions {
//         vote_threshold: 40,
//         suppression_radius: 8,
//     };
//     let lines: Vec<PolarLine> = detect_lines(&edges, options);

//     let white = Rgb::<u8>([255, 255, 255]);
//     let green = Rgb::<u8>([0, 255, 0]);
//     let black = Rgb::<u8>([0, 0, 0]);

//     // Convert edge image to colour
//     let color_edges = map_pixels(&edges, |_x, _y, p| if p[0] > 0 { white } else { black });

//     // Draw lines on top of edge image
//     let lines_image = draw_polar_lines(&color_edges, &lines, green);
//     // lines_image.save("output.png").unwrap();
//     let mut buf: Cursor<Vec<u8>> = Cursor::new(Vec::new());
//     lines_image
//         .write_to(&mut buf, image::ImageFormat::Png)
//         .unwrap();
//     buf.get_ref().to_vec()
// }
