import axios from "axios";

export async function generateImage(prompt, watermark = true) {
    const response = await axios.post("http://localhost:8000/generate-image/", {
        prompt,
        watermark
    });
    return response.data.image;
}
