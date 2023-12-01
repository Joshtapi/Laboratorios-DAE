import { useState } from "react";
import AuthService from "../services/auth.service";
import { useNavigate, Link } from "react-router-dom";
import "./login.css";

function Login() {
  const nav = useNavigate();
  const [message, setMessage] = useState("");
  const [usuario, setUsuario] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    console.log('usuario : ' + usuario);
    console.log('password : ' + password);

    AuthService.login(usuario, password)
      .then(() => {
        nav("/");
      })
      .catch((error) => {
        setMessage('Datos no válidos');
        console.log(error);
      });
  };

  return (
    <>
      <form onSubmit={handleSubmit}>
        <div className="form-floating mb-3">
          <input
            className="form-control"
            id="inputText"
            type="text"
            placeholder="usuario"
            value={usuario}
            onChange={(e) => setUsuario(e.target.value)}
          />
          <label htmlFor="inputText">Usuario</label>
        </div>
        <div className="form-floating mb-3">
          <input
            className="form-control"
            id="inputPassword"
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <label htmlFor="inputPassword">Password</label>
        </div>
        <div className="form-check mb-3">
          <input
            className="form-check-input"
            id="inputRememberPassword"
            type="checkbox"
            value=""
          />
          <label className="form-check-label" htmlFor="inputRememberPassword">
            Remember Password
          </label>
        </div>
        <div className="d-flex align-items-center justify-content-between mt-4 mb-0">
          <Link className="small" to="/password">
            Forgot Password?
          </Link>
          <input type="submit" className="btn btn-primary" value="Login" />
        </div>
      </form>
      
      {message && (
        <p className="text-center p-2 bg-red-100 text-red-800">
          {message}
        </p>
      )}
    </>
  );
}

export default Login;
