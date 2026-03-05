import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'
import Login from './pages/login'
import HomeUser from './pages/user/home'
import HomeAdmin from './pages/admin/home'
import Cadastro from './pages/register'
import AdminRoute from './routes/AdminRoute'
import PrivateRoute from './routes/PrivateRoute'  

const App = ()=>{
  return(
    <Router>
      <Routes>
        <Route path='/' element={<Login/>}/>
        <Route path='/login' element={<Login/>}/>
        <Route path='/register' element={<Cadastro/>}/>

        <Route 
          path='/user/home/' 
          element={
            <PrivateRoute>
              <HomeUser/>
            </PrivateRoute>
          }
        />

        <Route 
          path='/admin/home/' 
          element={
            <AdminRoute>
              <HomeAdmin/>
            </AdminRoute>
            }
          />

      </Routes>
    </Router>
  )
}

export default App;