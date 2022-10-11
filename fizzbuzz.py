'''
Regras do jogo FizzBuzz

1 - Se a posição for múltipla de 3 = Fizz
2 - Se a posição for múltipça de 5 = Buzz
3 - Se a posição for múltipla de 3 e de 5 = FizzBuzz
4 - Para qualquer outra posição fala o próprio número.
5 -  Números contendo ambos os algarismos devem aparecer como 'FizzBuzz', se o 3 vier antes do 5 ou 'BuzzFizz' caso contrário

- Kelver
- André

'''
import pytest
    

def robot(num):
  say = str(num)
  index = say.find('3')

  if str(5) in say[0:index]:
    return 'BuzzFizz'
      
  elif num % 3 == 0 and num % 5 == 0:
    return 'FizzBuzz'

  elif num  % 3 == 0 :
    return 'Fizz'

  elif num % 5 == 0:
    return 'Buzz'

  return num


if __name__ == "__main__":
    assert robot(1)      == 1
    assert robot(2)      == 2
    assert robot(4)      == 4
    assert robot(3)      == 'Fizz'
    assert robot(6)      == 'Fizz'
    assert robot(9)      == 'Fizz'
    assert robot(5)      == 'Buzz'
    assert robot(10)     == 'Buzz'
    assert robot(20)     == 'Buzz'
    assert robot(15)     == 'FizzBuzz'
    assert robot(30)     == 'FizzBuzz'
    assert robot(45)     == 'FizzBuzz'
    assert robot(53)     == 'BuzzFizz'
    assert robot(535)    == 'BuzzFizz'
    assert robot(453210) == 'BuzzFizz'
  
   
    pytest.main(['-svv', __file__])