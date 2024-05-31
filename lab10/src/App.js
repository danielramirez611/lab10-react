import React, { Component } from 'react';
import './App.css';
import {
  AppBar,
  Toolbar,
  Typography,
  Container,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  CircularProgress
} from '@mui/material';
import { styled } from '@mui/system';

const Logo = styled('img')({
  width: '50px',
  marginRight: '20px',
});

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      productos: [],
      recuperado: false
    }
  }

  componentDidMount() {
    fetch('http://127.0.0.1:8000/productos/')
      .then((response) => response.json())
      .then((prod) => {
        this.setState({ 
          productos: prod,
          recuperado: true 
        })
      })
  }

  render() {
    return (
      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>ID</TableCell>
              <TableCell>Nombre</TableCell>
              <TableCell>Precio</TableCell>
              <TableCell>Stock</TableCell>
              <TableCell>Fecha de Publicación</TableCell>
              <TableCell>Imagen</TableCell>
              <TableCell>Categoría</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {this.state.productos.map((producto) => (
              <TableRow key={producto.id}>
                <TableCell>{producto.id}</TableCell>
                <TableCell>{producto.nombre}</TableCell>
                <TableCell>{producto.precio}</TableCell>
                <TableCell>{producto.stock}</TableCell>
                <TableCell>{new Date(producto.pub_date).toLocaleDateString()}</TableCell>
                <TableCell>
                  <img src={`http://127.0.0.1:8000${producto.img_producto}`} alt={producto.nombre} style={{ width: '50px' }} />
                </TableCell>
                <TableCell>{producto.categoria}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    );
  }

  
}

export default App;
