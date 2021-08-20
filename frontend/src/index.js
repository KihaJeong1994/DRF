import React from 'react';
import ReactDOM from 'react-dom';
//import * as serviceWorker from './serviceWorker';
import './index.css';
import { Route, BrowserRouter as Router, Switch } from 'react-router-dom';
import App from './App';
//import reportWebVitals from './reportWebVitals';
import Header from './components/Header';
import Footer from './components/Footer';
import Register from './components/register';
import Login from './components/login';
import Logout from './components/logout';
import Single from './components/single';


const routing = (
<Router>
  <React.StrictMode>
    <Header/>
    <Switch>
      <Route exact path="/" component={App}/>
      <Route exact path="/register" component={Register}/>
      <Route exact path="/login" component={Login}/>
      <Route exact path="/logout" component={Logout}/>
      <Route exact path="/post/:slug" component={Single}/>
    </Switch>
    <Footer/>
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
