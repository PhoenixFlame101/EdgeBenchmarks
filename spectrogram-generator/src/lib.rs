// Finding spectrogram magnitudes from a given .wav file

#[cfg(target_family = "wasm")]
mod spectrogram;

#[cfg(target_family = "wasm")]
use serde::{Deserialize, Serialize};

#[cfg(target_family = "wasm")]
use spin_sdk::http::conversions::TryIntoBody;
#[cfg(target_family = "wasm")]
use spin_sdk::http::{IntoResponse, Request};
#[cfg(target_family = "wasm")]
use spin_sdk::http_component;

#[cfg(target_family = "wasm")]
#[derive(Deserialize)]
struct AudioRequest {
    audio_data: Vec<u8>, // Raw image bytes
}

#[cfg(target_family = "wasm")]
#[derive(Serialize)]
struct AudioResponse {
    audio_data: Vec<Vec<f32>>, // Spectrogram magnitudes
}

#[cfg(target_family = "wasm")]
#[http_component]
fn handle_upload(req: Request) -> anyhow::Result<impl IntoResponse> {
    let audio_request: AudioRequest = serde_json::from_slice(req.body()).unwrap();
    println!("Handling request to {:?}", req.header("spin-full-url"));

    match spectrogram::read_audio_file(&audio_request.audio_data) {
        Ok(audio_data) => {
            let spectrogram = spectrogram::generate_spectrogram(&audio_data);
            let response = AudioResponse {
                audio_data: spectrogram,
            };
            let response_json = spin_sdk::http::Json(response);
            Ok(spin_sdk::http::Response::builder()
                .status(200)
                .header("content-type", "application/json")
                .body(response_json.try_into_body().unwrap())
                .build())
        }
        Err(e) => {
            eprintln!("Failed to convert image: {}", e);
            Ok(spin_sdk::http::Response::builder().status(415).build())
        }
    }
}
