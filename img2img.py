import torch
import requests
from PIL import Image
from io import BytesIO

from diffusers import StableDiffusionImg2ImgPipeline

# load the pipeline
device = "cuda"
pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
    "./stable-diffusion-v1-5", revision="fp16", torch_dtype=torch.float16
).to(device)

# let's download an initial image
url = "https://cdn.discordapp.com/attachments/844700472820760576/1043294063060848743/MicrosoftTeams-image.png"

response = requests.get(url)
init_image = Image.open(BytesIO(response.content)).convert("RGB")
init_image = init_image.resize((768, 512))

#prompt = "a manga panel of a superhero, black and white, extremely detailed"

prompt = "a manga panel of a bald superhero wearing a belt, a cape, and boots, standing in front of a city landscape, extremely detailed"

images = pipe(prompt=prompt, init_image=init_image, strength=0.85, guidance_scale=7.5).images

images[0].save("newer_opm.png")
