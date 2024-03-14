class Llibre (var nom: String, var autor: String, var quantitat: Int){
    fun informacio() {}
}


class main() {
    val llibre1 = Llibre("Paco", "Zawar", 5)
    val llibre2 = Llibre("PAMPAM", "Adil", 2)
    
    val soci1 = Soci("Pedro", "Panflina", "123")
    val soci2 = Soci("Marco", "Polo", "456")
    
    val prestec1 = Prestec(llibre1, soci1, "2024-03-14")
    val prestec2 = Prestec(llibre2, soci2, "2023-03-14")

    prestec1.registrarPrestec()
    llibre1.informacio()
    soci2.informacio()
    prestec1.retornarPrestec()
    llibre1.informacio()
}
