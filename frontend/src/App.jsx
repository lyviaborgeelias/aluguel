import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'
import Login from './pages/login'
import HomeUser from './pages/home_user'
import Cadastro from './pages/register/index'

const App = ()=>{
  return(
    <Router>
      <Routes>
        <Route path='/' element={<Login/>}/>
        <Route path='/login' element={<Login/>}/>
        <Route path='/homeuser' element={<HomeUser/>}/>
        <Route path='/register' element={<Cadastro/>}/>
      </Routes>
    </Router>
  )
}

export default App;