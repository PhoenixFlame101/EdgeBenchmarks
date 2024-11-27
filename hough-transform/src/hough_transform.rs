// Portions of this file are adapted from the imageproc crate (https://github.com/image-rs/imageproc)
// Said code is licensed with The MIT License (MIT), Copyright (c) 2015 PistonDevelopers

use std::io::Cursor;

use image::{DynamicImage, Rgb};
use imageproc::edges::canny;
use imageproc::hough::{detect_lines, draw_polar_lines, LineDetectionOptions, PolarLine};
use imageproc::map::map_pixels;

pub fn get_features(input_image: DynamicImage) -> Vec<u8> {
    // Load image and convert to grayscale
    let input_image = input_image.to_luma8();

    // Detect edges using Canny algorithm
    let edges = canny(&input_image, 50.0, 100.0);

    // Detect lines using Hough transform
    let options = LineDetectionOptions {
        vote_threshold: 40,
        suppression_radius: 8,
    };
    let lines: Vec<PolarLine> = detect_lines(&edges, options);

    let white = Rgb::<u8>([255, 255, 255]);
    let green = Rgb::<u8>([0, 255, 0]);
    let black = Rgb::<u8>([0, 0, 0]);

    // Convert edge image to colour
    let color_edges = map_pixels(&edges, |_x, _y, p| if p[0] > 0 { white } else { black });

    // Draw lines on top of edge image
    let lines_image = draw_polar_lines(&color_edges, &lines, green);
    // lines_image.save("output.png").unwrap();
    let mut buf: Cursor<Vec<u8>> = Cursor::new(Vec::new());
    lines_image
        .write_to(&mut buf, image::ImageFormat::Png)
        .unwrap();
    buf.get_ref().to_vec()
}
