import React from "react";
import { Link } from "react-router-dom";

function NotFound() {
  return (
    <div className="container">
      <div className="row justify-content-center">
        <div className="col-lg-6">
          <div className="text-center mt-4">
            <img
              className="mb-4 img-error"
              src="https://cdn-icons-png.flaticon.com/512/1548/1548682.png"
              alt="Error"
            />
            <p className="lead">Esta URL solicitada no se encontró en este servidor.</p>
            <Link to="/">Regresar al Inicio</Link>
          </div>
        </div>
      </div>
    </div>
  );
}

export default NotFound;
