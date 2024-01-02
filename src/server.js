import express from 'express'
import session from 'express-session'
import helmet from 'helmet'
import { dirname, join } from 'node:path'
import { fileURLToPath } from 'node:url'
import { router } from './routes/router.js'
import 'dotenv/config'



try {
  const directoryFullName = dirname(fileURLToPath(import.meta.url))

  const app = express()
  app.use(helmet())
  app.use(express.json())
  app.set('view engine', 'ejs')
  app.set('views', join(directoryFullName, 'views'))
  app.use(express.static(join(directoryFullName, '..', 'public')))
  app.use(express.urlencoded({ extended: false }))

app.use(session({
    secret: process.env.SESSION_SECRET,
    resave: false,
    saveUninitialized: false,
    cookie: {
        secure: false, // if true only transmit cookie over https
        httpOnly: false, // if true prevent client side JS from reading the cookie 
        maxAge: 1000 * 60 * 10 // session max age in miliseconds
    }
}))

  app.listen(process.env.PORT || 8084, () => {
    console.log(`Server running at http://localhost:${process.env.PORT || 8084}`)
  })
  app.use('/', router)
  
} catch(error) {
  console.log(error)
}