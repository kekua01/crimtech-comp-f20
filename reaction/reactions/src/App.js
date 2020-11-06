import logo from './logo.svg';
import './App.css';
import React from 'react';

class Panel extends React.Component {
  constructor(props) {
    super(props);
    this.state = { start_time: 0, ran_once: false, counting: false, true_duration: 0, reaction_time: 0, color: 'green'};
    this.process_click = this.process_click.bind(this);
    this.start_count = this.start_count.bind(this);
  }
  handle_color = (c) => {
    console.log(this.state.true_duration);
    setTimeout(() => {
        this.setState({color: c})
    }, this.state.true_duration);
  }
  start_count() {
    this.setState({
      start_time: window.performance.now(),
      counting: true,
      true_duration: 1000 * ((Math.random() * 5) + 2),
      color: 'red'
    },
     () => {this.handle_color('green')
   });
    
  }
  end_count() {
    let secs_passed = window.performance.now() - this.state.start_time
    if (secs_passed >= this.state.true_duration) {
      this.setState({
        ran_once: true,
        counting: false,
        reaction_time: (secs_passed - this.state.true_duration).toFixed(2)
      })
    }
  }
  process_click() {
    if (this.state.counting) {
      this.end_count();
    } else this.start_count();
  }
  render() {
    let msg = "Click me to begin";
    if (this.state.counting) {
      if (this.state.color == 'red') {
        msg = "Wait for green"
      }
      else {
        msg = "Click!"
      }
    }
    else if (this.state.ran_once) {
      msg = "Your reaction time is " + this.state.reaction_time + " ms."
    }
    return (
      <div className = "PanelContainer" onClick = {this.process_click} style={ { background: this.state.color} }>
        <div className = "Panel">{msg}</div>
      </div>
    );
  }
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1 className =  "Header">How Fast is your Reaction Time?</h1>
        <Panel />
        <p>Click as soon as the red box turns green. Click anywhere in the box to start.</p>
      </header>
    </div>
  );
}

export default App;
