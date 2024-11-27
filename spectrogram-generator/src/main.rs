// Finding spectrogram magnitudes from a given .wav file

#[cfg(not(target_family = "wasm"))]
mod spectrogram;

#[cfg(not(target_family = "wasm"))]
use serde::{Deserialize, Serialize};
#[cfg(not(target_family = "wasm"))]
use warp::Filter;

#[cfg(not(target_family = "wasm"))]
#[derive(Deserialize)]
struct AudioRequest {
    audio_data: Vec<u8>, // Raw image bytes
}

#[cfg(not(target_family = "wasm"))]
#[derive(Serialize)]
struct AudioResponse {
    audio_data: Vec<Vec<f32>>, // Spectrogram magnitudes
}

#[cfg(not(target_family = "wasm"))]
#[tokio::main]
async fn warp_server() {
    let upload = warp::post()
        .and(warp::path("upload"))
        .and(warp::header::exact("content-type", "application/json"))
        .and(warp::body::json())
        .map(|audio_request: AudioRequest| {
            let audio_data = spectrogram::read_audio_file(&audio_request.audio_data).unwrap();
            let spectrogram = spectrogram::generate_spectrogram(&audio_data);
            let response = AudioResponse {
                audio_data: spectrogram,
            };
            warp::reply::json(&response)
        });

    // Start the warp server
    println!("Listening on http://0.0.0.0:3000...");
    warp::serve(upload).run(([0, 0, 0, 0], 3000)).await;
}

fn main() {
    #[cfg(not(target_family = "wasm"))]
    warp_server();
}
