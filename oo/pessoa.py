class Pessoa:
    def cumprimentar(self):
        return f"Ola {id(p)}"

if __name__== '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p)) # igual a linha 9
    print(id(p))
    print(p.cumprimentar()) 