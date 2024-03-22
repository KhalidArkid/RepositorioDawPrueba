import libro.Libro
import prestamo.Prestamo

class Socio(val nombre: String, val apellido: String, val identificador: Int) {
    fun solicitarPrestamo(libro: Libro, fechaPrestamo: String) {
        println("Prestamo solicitado por $nombre $apellido, id: $identificador")
        val prestamo = Prestamo(libro, this)
        prestamo.registrarPrestamo(fechaPrestamo)
    }

    fun devolverPrestamo() {
        println("Devolucion de prestamo por $nombre $apellido, id: $identificador")
        val prestamo = Prestamo(libro, this)
        prestamo.devolverPrestamo()
    }

    fun informacion() {
        println("nombre: $nombre, apellido: $apellido, numero de socio: $identificador")
    }
}

