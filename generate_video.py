import imageio.v2 as imageio
import os

def gerar_video_com_imageio(frames_dir="frames", output_file="scroll_video.mp4", fps=10):
    # Lista e ordena os arquivos de frame
    imagens = sorted([
        os.path.join(frames_dir, nome)
        for nome in os.listdir(frames_dir)
        if nome.endswith(".png")
    ])

    if not imagens:
        print("Nenhuma imagem encontrada em", frames_dir)
        return

    # Lê a primeira imagem para obter o tamanho
    exemplo = imageio.imread(imagens[0])
    altura, largura = exemplo.shape[:2]

    writer = imageio.get_writer(output_file, fps=fps)

    for imagem_path in imagens:
        frame = imageio.imread(imagem_path)
        writer.append_data(frame)

    writer.close()
    print(f"🎞️ Vídeo criado com sucesso: {output_file}")

gerar_video_com_imageio()