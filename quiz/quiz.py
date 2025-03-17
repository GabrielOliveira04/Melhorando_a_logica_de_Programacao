import json
import random
import time

 

def carregar_perguntas():
    with open("perguntas.json",encoding="utf-8" ) as p:
      perguntas = json.load(p)["perguntas"]
      
      return perguntas

def selecionar_perguntas(questions, num_questions):
   if num_questions > len(questions):
      num_questions = len(questions)
   
   random_question = random.sample(questions, num_questions) 
   return random_question      
        


def imprimir_perguntas(pergunta):
   print(pergunta["pergunta"])
   for i, alternativas in enumerate(pergunta["alternativas"]) :
        print(str(i + i) + ".", alternativas)

   numero = int(input(" Selecione O número correto: "))
   if numero < 1 or numero > len(pergunta["alternativas"]):
      print("Deu errado")     
      return False
   
   acerto = pergunta["alternativas"][numero - 1] == pergunta["correta"]
   if acerto == True:
      print("Parabéns, você acertou")
   return acerto

        
    



pergunta = carregar_perguntas()
total_perguntas = int(input("Digite o numero de perguntas :"))
random_questions = selecionar_perguntas(pergunta, total_perguntas) 
correta = 0
start_time = time.time()


for pergunta in random_questions:
   is_correct =imprimir_perguntas(pergunta)
   if is_correct:
      correta += 1
      
   print("------------------------------")
   
completed_time = time.time() - start_time      
print("Resumo")
print(f"Total de perguntas : {total_perguntas}")
print("Questões acertadas", correta)
print("Pontos", str(round((correta / total_perguntas)* 100, 2) )+ "%")