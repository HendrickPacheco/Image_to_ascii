import PIL.Image

# caracteres ascii que irão construir a saída de texto
# Um pixel mais escuro será traduzido em "@" e um mais claro em "."
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# Redimensionando a imagem de acordo com a nova altura


class FormatImage:
    def resize_image(self, image, nova_largura=100):
        largura, altura = image.size  # Pega a largura e a altura da imagem
        razao = altura / largura  # proporção entre altura e largura
        nova_altura = int(nova_largura * razao)
        # image.resize() retorna um objeto Image
        nova_imagem = image.resize((nova_largura, nova_altura))
        return nova_imagem

    # Convertendo cada pixel para escalas de cinza
    def tornar_cinza(self, image):
        escala_cinza = image.convert("L")
        return escala_cinza

    # Convertendo pixels para String
    def pixel_para_ascii(self, image):
        # Retorna o conteúdo desta imagem como um objeto de sequência contendo valores de pixel.
        pixels = image.getdata()
        caracteres = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
        return caracteres


class MakeImage(FormatImage):
    def main(self, nova_largura=100):
        # Abrir a imagem atraves da entrada do ususario
        path = input("Digite o caminho da imagem:\n")
        try:
            image = PIL.Image.open(path)
        except:
            print(path, "Esse não é o caminho correto.")

        # Convertendo imagem para ASCII
        new_image_data = self.pixel_para_ascii(self.tornar_cinza(self.resize_image(image)))

        # Formatando
        pixel_count = len(new_image_data)
        ascii_image = "\n".join(
            new_image_data[i:i + nova_largura] for i in range(0, pixel_count, nova_largura))

        # Printar o resultado
        print(ascii_image)

        # Salvando o Resultado no "ascii_image.txt"
        with open("ascii_image.json", "w") as f:
            f.write(ascii_image)


MakeImage().main()
