class Libro(val titulo: String, val autor: String, var cantidad: Int) {
    fun prestar() {
        if (cantidad > 0) {
            cantidad--
            println("Libro prestado: $titulo, autor: $autor")
        } else {
            println("No hay ejemplares de $titulo")
        }
    }

    fun devolver() {
        cantidad++
        println("Libro devuelto: $titulo, autor: $autor")
    }

    fun informacion() {
        println("titulo: $titulo, autor: $autor, ejemplares disponibles: $cantidad")
    }
}

