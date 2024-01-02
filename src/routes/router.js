import express from 'express'
import { SearchController } from '../controllers/search-controller.js'

export const router = express.Router()
const controller = new SearchController()

router.get('/', (req, res, next) => {
  controller.getStart(req, res)
})

router.post('/data', (req,res,next) => {
  controller.fetchSearchResult(req, res)
})