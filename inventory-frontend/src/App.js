import {Products} from "./components/Products";
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import {ProductsCreate} from "./components/ProductsCreate";
import {Orders} from "./components/Orders";
import {Users} from "./components/Users";
import {Login} from "./components/Login";

function App() {
    return <BrowserRouter>
        <Routes>
            <Route path="/" element={<Login/>}/>
            <Route path="/products" element={<Products/>}/>
            <Route path="/create" element={<ProductsCreate/>}/>
            <Route path="/orders" element={<Orders/>}/>
            <Route path="/users" element={<Users/>}/>
        </Routes>
    </BrowserRouter>;
}

export default App;
