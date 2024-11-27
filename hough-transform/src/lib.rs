// Finding lines in a greyscale image using hough transform

#[cfg(target_family = "wasm")]
mod hough_transform;

#[cfg(target_family = "wasm")]
use serde::Deserialize;

#[cfg(target_family = "wasm")]
use spin_sdk::http::{IntoResponse, Request};
#[cfg(target_family = "wasm")]
use spin_sdk::http_component;

#[cfg(target_family = "wasm")]
#[derive(Deserialize, Debug)]
struct ImageRequest {
    image_data: Vec<u8>, // Raw image bytes
}

#[cfg(target_family = "wasm")]
#[http_component]
fn handle_upload(req: Request) -> anyhow::Result<impl IntoResponse> {
    use spin_sdk::http::Response;

    println!("Handling request to {:?}", req.header("spin-full-url"));
    let response_json: ImageRequest = serde_json::from_slice(req.body()).unwrap();

    match image::load_from_memory(&response_json.image_data) {
        Ok(dynamic_image) => {
            // Get the lines features and send back a success code
            let image_bytes = hough_transform::get_features(dynamic_image);
            Ok(Response::builder()
                .status(200)
                .header("content-type", "image/png")
                .body(image_bytes)
                .build())
        }
        Err(e) => {
            eprintln!("Failed to convert image: {}", e);
            Ok(Response::builder().status(415).build())
        }
    }
}
