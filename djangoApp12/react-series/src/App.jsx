import React, { useState, useEffect } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import Table from 'react-bootstrap/Table';
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

function App() {
  const [series, setSeries] = useState([]);
  const [pos, setPos] = useState(null);
  const [titulo, setTitulo] = useState('Nuevo');
  const [id, setId] = useState(0);
  const [nombre, setNombre] = useState('');
  const [fecha, setFecha] = useState('');
  const [rating, setRating] = useState(0);
  const [categoria, setCategoria] = useState('');

  useEffect(() => {
    // Realizar la llamada a la API para obtener los datos iniciales
    axios.get('http://localhost:8000/serie')
      .then(res => {
        setSeries(res.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);


  function mostrar(cod, index) {
    axios.get(`http://localhost:8000/serie/${cod}`)
      .then(res => {
        setPos(index);
        setTitulo('Editar');
        setId(res.data.id);
        setNombre(res.data.name);
        setFecha(res.data.release_date);
        setRating(res.data.rating);
        setCategoria(res.data.category);
      })
      .catch(error => {
        console.error(error);
      });
  }

  function guardar(e) {
    e.preventDefault();
    let cod = id;
    let datos = {
      name: nombre,
      release_date: fecha,
      rating: rating,
      category: categoria
    };
    if (cod > 0) {
      axios.put(`http://localhost:8000/serie/${cod}`, datos)
        .then(res => {
          let indx = pos;
          series[indx] = res.data;
          var temp = [...series];
          setPos(null);
          setTitulo('Nuevo');
          setId(0);
          setNombre('');
          setFecha('');
          setRating(0);
          setCategoria('');
          setSeries(temp);
        })
        .catch(error => {
          console.log(error.toString());
        });
    } else {
      axios.post('http://localhost:8000/serie', datos)
        .then(res => {
          var temp = [...series];
          temp.push(res.data);
          setPos(null);
          setTitulo('Nuevo');
          setId(0);
          setNombre('');
          setFecha('');
          setRating(0);
          setCategoria('');
          setSeries(temp);
        })
        .catch(error => {
          console.log(error.toString());
        });
    }
  }

  function eliminar(cod) {
    let rpta = window.confirm('¿Desea eliminar?');
    if (rpta) {
      axios.delete(`http://localhost:8000/serie/${cod}`)
        .then(res => {
          var temp = series.filter(serie => serie.id !== cod);
          setSeries(temp);
        })
        .catch(error => {
          console.error(error);
        });
    }
  }


  return (
    <div>
      <Container>
        <Table striped bordered hover variant="dark">
          <thead>
            <tr>
              <th>#</th>
              <th>Nombre</th>
              <th>Fecha</th>
              <th>Rating</th>
              <th>Categoria</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {series.map((serie, index) => (
              <tr key={serie.id}>
                <td>{serie.id}</td>
                <td>{serie.name}</td>
                <td>{serie.release_date}</td>
                <td>{serie.rating}</td>
                <td>{serie.category}</td>
                <td>
                  <button style={{ marginRight: '10px' }} class="btn btn-success edit-button" onClick={() => mostrar(serie.id, index)}>Editar</button>
                  <button class="btn btn-danger delete-button" onClick={() => eliminar(serie.id)}>Eliminar</button>
                </td>
              </tr>
            ))}
          </tbody>
        </Table>
        <hr />
        <h1>{titulo}</h1>
        <Form onSubmit={guardar}>
          <Form.Control type="hidden" value={id} />
          <Form.Group className="mb-3">
            <Form.Label>Ingrese Nombre:</Form.Label>
            <Form.Control type="text" value={nombre} onChange={e => setNombre(e.target.value)} />
          </Form.Group>
          <Form.Group className="mb-3">
            <Form.Label>Ingrese Rating:</Form.Label>
            <Form.Control type="number" value={rating} onChange={e => setRating(e.target.value)} />
          </Form.Group>
          <Form.Group className="mb-3">
            <Form.Label>Categoria:</Form.Label>
            <Form.Control as="select" value={categoria} onChange={e => setCategoria(e.target.value)}>
              <option value="">Seleccionar categoría</option>
              <option value="comedy">Comedia</option>
              <option value="drama">Drama</option>
              <option value="action">Acción</option>
              <option value="horror">Horror</option>
            </Form.Control>
          </Form.Group>
          <Form.Group className="mb-3">
            <Form.Label>Fecha:</Form.Label>
            <Form.Control type="date" value={fecha} onChange={e => setFecha(e.target.value)} />
          </Form.Group>
          <Button variant="primary" type="submit">
            GUARDAR
          </Button>
        </Form>
      </Container>
    </div>
  );
}

export default App;