import libro.Libro
import socio.Socio

class Prestamo(private val libro: Libro, private val socio: Socio) {
    fun registrarPrestamo(fecha: String) {
        println("Prestamo registrado: Libro ${libro.titulo}, Socio ${socio.nombre}, Fecha: $fecha")
        libro.prestar()
    }

    fun devolverPrestamo() {
        println("Devolucion de Prestamo: Libro ${libro.titulo}, Socio ${socio.nombre}")
        libro.devolver()
    }

    fun informacion() {
        println("Prestamo del libro ${libro.titulo} al socio ${socio.nombre} ${socio.apellido}")
    }
}

