
import { Route, Routes } from 'react-router-dom'

import { AutoParks, Login } from './components'
// import { useEffect } from 'react'
// import { autoParkService } from './services'

const App = () => {
  // useEffect(()=>{
  //   autoParkService.getCarsById(1).then(value => console.log(value))
  // },[])
  return (
    <div>
      <Routes>
        <Route path={'/'} element={<Login/>}/>
        <Route path={'auto_parks'} element={<AutoParks/>}/>
      </Routes>
    </div>
  )
}

export { App }