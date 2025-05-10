import React  from "react";

const Navbar = () => {

    return (
        <nav className="bg-gray-800 text-white p-4">
            <div className="container mx-auto flex justify-between items-center">
            <h1 className="text-xl font-bold"> Ejemplo </h1>
            <ul className="flex space-x-4">
            <li>
                <a href="/Create">Crear</a>
            </li>
            <li>
                <a href="/Home">Home</a>
            </li>
            </ul>

            </div>
        </nav>
    )
}
export default Navbar;