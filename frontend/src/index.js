import React from 'react';
import ReactDOM from 'react-dom';
//import * as serviceWorker from './serviceWorker';
import './index.css';
import { Route, BrowserRouter as Router, Switch } from 'react-router-dom';
import App from './App';
//import reportWebVitals from './reportWebVitals';
import Header from './components/Header';


const routing = (
<Router>
  <React.StrictMode>
    <Header/>
    <Switch>
      <Route exact path="/" component={App}/>
    </Switch>
    
  </React.StrictMode>
</Router>
)

ReactDOM.render(
  routing,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
//serviceWorker.unregister();