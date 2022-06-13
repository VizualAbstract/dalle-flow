# Dall-E

## Docker steps

```bash
docker build --build-arg GROUP_ID=$(id -g ${USER}) --build-arg USER_ID=$(id -u ${USER}) -t jinaai/dalle-flow .
```

```bash
docker run -p 51005:51005 -v $HOME/.cache:/home/dalle/.cache --gpus all jinaai/dalle-flow
```

## Configuration steps

```bash
python
```

```python
server_url = 'grpc://localhost:51005'
server_url = 'grpc://localhost:57867'
server_url = 'grpc://localhost:65282'
```

```python
prompt = 'an oil painting of a humanoid robot playing chess in the style of Matisse'
```

```python
from docarray import Document

da = Document(text=prompt).post(server_url, parameters={'num_images': 1}).matches

da.plot_image_sprites(fig_size=(10,10), show_index=True)
```

<!-- end support-pitch -->