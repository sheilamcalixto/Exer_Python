## Criando um sistema de recomendção de curso.


nome = input("Como gostraia de ser chamado(a): ")
categorias = ["Ciências Biológicas Modalidade Microbiologia e Imunologia.",
              "Comunicação Social.",
              "Composição Paisagística.",
              "Composição de Interior.",
              "Ciências Sociais.",
              "Ciências Econômicas.",
              "Ciências Contábeis.",
              "Ciências Biológicas Modalidade Médica.",
              "Administração.",
              "Contabilidade e Economia.",
              "Direito.",
              "Informática."]

cursos = ["Ciências Biológicas Modalidade Microbiologia e Imunologia.",
          "Comunicação Social.",
          "Composição Paisagística.",
          "Composição de Interior.",
          "Ciências Sociais.",
          "Ciências Econômicas.",
          "Ciências Contábeis.",
          "Ciências Biológicas Modalidade Médica.",
          "Administração.",
          "Contabilidade e Economia.",
          "Direito.",
          "Informática."]

tempos = [95,
          25,
          200,
          35,
          45,
          100,
          20,
          120,
          324,
          400,
          29]

categorias_do_curso = [
    ['curso livre'],
    ['Profissional'],
    ['Graduação'],
    ['Iniciante'],
    ['Básico'],
    ['Profissional'],
    ['Curso livre'],
    ['Básico'],
    ['Doutorado'],
    ['Bacharelado'],
    ['Mestrado']

]

gratuidade = [True,
              False,
              False,
              True,
              True,
              True,
              True,
              False,
              False,
              False,
              True, ]




for i in range(len(categorias)):
    print(f'{i}.  {categorias[i]}')

num_das_categorias = input("Digite o número dos assuntos de seu interesse (separe por vírgula): \n")

tempo = float(input("Quanto tempo gostaria de estudar? (min)\n"))

mostrar_premium = input("Mostrar cursos Premium (S/N)?\n")

if mostrar_premium == "N" or mostrar_premium != "n":
    mostrar_premium = False

elif mostrar_premium == "S" or mostrar_premium == "s":
    mostrar_premium = True

num_das_categorias = num_das_categorias.split(",")
ncategorias = []
for elemento in num_das_categorias:
    numero = int(elemento.strip())
    ncategorias.append(numero)
print(f"Nome:{nome}")
print(f"ID das categorias: {ncategorias}")
print(f"Tempo: {tempo}")
print(f"Premium?: {mostrar_premium}")

print(ncategorias)


categorias_selecionada = []

for n in ncategorias:
    categorias_selecionada.append(categorias[n].upper())
print(f"Olá, {nome}, com base no seu perfil, achamos que você iria gostar dos seguintes cursos:")
for cat in categorias_selecionada:
  print(f"{cat}:")
  for linha in range(len(cursos)):
    if gratuidade[linha] or mostrar_premium:
      if (cat.lower() in categorias_do_curso[linha]
          and tempos[linha] <= tempo):
        print(f"– {cursos[linha]} ({tempos[linha]} min)")

print(categorias_selecionada)

