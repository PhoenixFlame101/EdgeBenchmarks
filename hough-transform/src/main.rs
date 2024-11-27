// Finding lines in a greyscale image using hough transform

#[cfg(not(target_family = "wasm"))]
mod hough_transform;

#[cfg(not(target_family = "wasm"))]
use serde::Deserialize;
#[cfg(not(target_family = "wasm"))]
use warp::Filter;

#[cfg(not(target_family = "wasm"))]
#[derive(Deserialize)]
struct ImageRequest {
    image_data: Vec<u8>, // Raw image bytes
}

#[cfg(not(target_family = "wasm"))]
#[tokio::main]
async fn warp_server() {
    let upload = warp::post()
        .and(warp::path("upload"))
        .and(warp::header::exact("content-type", "application/json"))
        .and(warp::body::json())
        .map(|image_request: ImageRequest| {
            // Convert the bytes to a DynamicImage
            match image::load_from_memory(&image_request.image_data) {
                Ok(dynamic_image) => {
                    // Get the lines features and send back the modified images
                    let image_bytes = hough_transform::get_features(dynamic_image);
                    warp::reply::with_status(image_bytes, warp::http::StatusCode::OK)
                }
                Err(e) => {
                    eprintln!("Failed to convert image: {}", e);
                    warp::reply::with_status(vec![], warp::http::StatusCode::UNSUPPORTED_MEDIA_TYPE)
                }
            }
        });

    // Start the warp server
    println!("Listening on http://0.0.0.0:3000...");
    warp::serve(upload).run(([0, 0, 0, 0], 3000)).await;
}

fn main() {
    #[cfg(not(target_family = "wasm"))]
    warp_server();
}
