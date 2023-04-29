import { axiosService } from './axios.service'
import { urls } from '../constants'

const autoParkService = {
  getAll:()=>axiosService.get(urls.autoParks),
  create:(autoPark)=>axiosService.post(urls.autoParks, autoPark),
  // getCarsById:(id)=>axiosService.get(`${urls.autoParks}/${id}/cars`)
}

export {
  autoParkService
}