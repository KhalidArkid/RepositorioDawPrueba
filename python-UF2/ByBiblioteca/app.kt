import libro.Libro
import socio.Socio

class App(val libro: Libro, val socio: Socio) {
    fun exec() {
        /*Crear libros*/
        val libro1: Libro = Libro("El senyor de los anillos", "J.R.R. Tolkien", 3)
        val libro2: Libro = Libro("1984", "George Orwell", 5)

        /*Crear socios*/
        val socio1: Socio = Socio("Unai", "Rosal", 101)
        val socio2: Socio = Socio("Oscar", "Gomez", 202)

        /*Realizar acciones*/
        libro1.informacion()
        socio2.informacion()
        socio1.solicitarPrestamo(libro1, "2024-03-15")
        libro1.informacion()
        socio2.devolverPrestamo(libro1)
        libro1.informacion()
    }
}

fun main() {
    val app = App()
    app.exec()
}