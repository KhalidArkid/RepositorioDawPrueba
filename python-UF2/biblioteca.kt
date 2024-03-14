
fun main() {
    val llibre = Llibre()
    val soci = Soci()
    val prestec = Prestec()

    prestec.registrarPrestec(llibre, soci, Date())

    println("Informació del llibre:")
    llibre.obtenirInformacio()

    println("Informació del soci:")
    soci.obtenirInformacio()

    println("Informació del préstec:")
    prestec.obtenirInformacio()

    prestec.retornarPrestec(llibre)
}
