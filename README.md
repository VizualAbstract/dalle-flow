# Dall-E

## Docker compose

Get the Dall-E server, backend API and frontend web app running using a single command

```bash
docker-compose up
```

(It will take about 15-20 minutes to complete the first time)

### URLs

- Frontend: <http://localhost:3000>
- Backend: <http://localhost:8080>
- Dall-E server: rpc://localhost:51005

## Configuration steps

Once the server is running, you can use the image service by opening a new terminal window and using the following commands to generate a single image

```bash
python
```

```python
server_url = 'grpc://localhost:51005'
```

```python
prompt = 'an oil painting of a humanoid robot playing chess in the style of Matisse'
```

```python
from docarray import Document

da = Document(text=prompt).post(server_url, parameters={'num_images': 1}).matches

da.plot_image_sprites(fig_size=(10,10), show_index=True)
```

### Select for Diffuse

```python
fav_id = 3
fav = da[fav_id]
fav.display()
```

### Diffuse

```python
diffused = fav.post(f'{server_url}', parameters={'skip_rate': 0.5, 'num_images': 36}, target_executor='diffusion').matches

diffused.plot_image_sprites(fig_size=(10,10), show_index=True)
```

### Select for Upscale

```python
dfav_id = 34
fav = diffused[dfav_id]
fav.display()
```

### Upscale

```python

fav = fav.post(f'{server_url}/upscale')
fav.display()
```

## Manual docker steps

```bash
docker build --build-arg GROUP_ID=$(id -g ${USER}) --build-arg USER_ID=$(id -u ${USER}) -t jinaai/dalle-flow .
```

```bash
docker run -p 51005:51005 -v $HOME/.cache:/home/dalle/.cache --gpus all jinaai/dalle-flow
```
