import { useEffect, useState } from 'react'
import { autoParkService } from '../../services'
import { AutoPark } from '../AutoPark/AutoPark'
import { AutoParkForm } from '../AutoParkForm/AutoParkForm'
import { Chat } from '../Chat/Chat'
import css from './AutoParks.module.css'
import { socketService } from '../../services/socket.service'

const AutoParks = () => {
  const [autoParks, setAutoParks] = useState([])
  const [chatSocket, setChatSocket] = useState(null)
  const [messages, setMessages] = useState([])

  useEffect(() => {
    autoParkService.getAll().then(value => value.data).then(value => setAutoParks([...value]))
  }, [])

  useEffect(() => {
    chatSocketInit().then(value => setChatSocket(value))
    autoParkSocketInit().then()
  }, [])

  const chatSocketInit = async () => {
    const client = await socketService.chat()

    client.onopen = () => {
      console.log('Chat socket connected')
    }
    client.onmessage = (msg) => {
      console.log(msg.data)
      setMessages(prev => [...prev, JSON.parse(msg.data)])
    }
    return client
  }
  const autoParkSocketInit = async () => {
    const client = await socketService.autoParks()

    client.onopen = () => {
      console.log('AutoParkSocket connected')
      client.send(JSON.stringify({
        action: 'subscribe_to_auto_park_activity',
        request_id: new Date().getTime()
      }))
    }

    client.onmessage=(msg)=>{
      const data = JSON.parse(`${msg.data}`)
      console.log(data)
      setAutoParks(prevState => [...prevState, msg.data])
    }
    return client
  }
  return (
    <div className={css.AutoParks}>
      <div>
        <AutoParkForm setAutoParks={setAutoParks}/>
        <hr/>
        <div>
          {autoParks.map(autoPark => <AutoPark key={autoPark.id} autoPark={autoPark}/>)}
        </div>
      </div>
      <Chat chatSocket={chatSocket} messages={messages}/>
    </div>
  )
}

export { AutoParks }