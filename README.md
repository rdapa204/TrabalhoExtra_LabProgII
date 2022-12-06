# TrabalhoExtra_LabProgII

Na soma de Wallis, temos um produtório de dois termos. Um é formado pelo produtório de números ligeramente maiores que um, tendo o produtório tendendo a infinito. O outro é formado pelo produtório de valores ligeramentes menores do que um, os quais tendem a zero. 

O curioso é que fazendo tal produtório de forma conjunta temos duas vezes pi! 

O programa implementa duas Threads para calcular os produtos parciais, até uma dada precisão fornecida pelo usuário, daí então armazena o resultado de cada Thread em variáveis globais. Após é cálculado o pi de Wallis de forma iterativa e é comparado o valor encontrado e o tempo gasto. 


Para valores maiores de precisão o método sequencial se mostrou mais rápido.
![image](https://user-images.githubusercontent.com/89489900/205892115-51369133-1792-46e1-b591-53d8e0245790.png)

Agora, já para valores menores de precisão o método de Thread foi mais rápido.
![image](https://user-images.githubusercontent.com/89489900/205891873-a8ef1ff9-dc8c-48e7-a06b-5a84e4cae488.png)


