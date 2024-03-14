class main() {
    val llibre = Llibre()
    val soci = Soci()
    val prestec = Prestec()

    prestec.registrarPrestec(llibre, soci, Date())

    println("Informació del llibre:")
    llibre.obtenirInformacio(llibre)

    println("Informació del soci:")
    soci.obtenirInformacio(soci)

    println("Informació del préstec:")
    prestec.obtenirInformacio(prestec)

    prestec.retornarPrestec(llibre)
}
