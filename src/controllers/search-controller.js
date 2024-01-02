import fetch from "node-fetch"

/**
 * Controller for searchengine.
 */
export class SearchController {
  constructor() {
    this.result
  }

  getStart(req, res) {
    const result = this.result
    res.render('index', { result })
  }

  async fetchSearchResult(req, res) {
    try {
      console.log(req.body.search)
      const response = await fetch("http://localhost:8080/search", {
          method : 'POST',
          headers: {
            'Accept' : 'application/json',
            'Content-Type' : 'application/json'
          },
          body : JSON.stringify({
            search : req.body.search,
          })
        })
      const result = await response.json()
      this.result = result
      res.redirect('.')
    } catch (error) {
      console.log(error)
    }
  }
}