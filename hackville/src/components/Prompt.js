import React, {useState} from 'react'
import Navbar from './Navbar2'
import './Prompt.css'
import { makeStyles } from '@material-ui/core/styles';
import Slider from '@material-ui/core/Slider';
const useStyles = makeStyles({
    root: {
        width: 300,
        display: 'flex',
        justifyContent: 'center',
        height: '100%',
        alignSelf: 'center',

    },
    customSlider: {
        '& .MuiSlider-thumb': {
            backgroundColor: 'white',
            border: `3px solid #3EE0B9`,
            position: 'relative',
            top: 0,
            width: 25,
            height: 25,
        },
        '& .MuiSlider-active': {
            color: '#3EE0B9',
        },
        '& .MuiSlider-track': {
            backgroundColor: '#3EE0B9',
            height: 15,
            width: 30,
        },
        '& .MuiSlider-rail': {
            backgroundColor: '#ECECEC',
            height: 13,
        },
    },
});






const Prompt = () => {
    const classes = useStyles();
    const [value1, setValue1] = useState(30);
    const [value2, setValue2] = useState(30);
    const [value3, setValue3] = useState(30);
    const [value4, setValue4] = useState('');


    // const handleChange = (event, newValue) => {
    //     setValue(newValue);
    //     console.log(value, "slider value")
    // };
    const marks = [
        {
            value: 1,
            label: '1',
        },
        {
            value: 100,
            label: '100',
        },
    ];

    const marks2 = [
        {
            value: 1,
            label: '1',
        },
        {
            value: 10,
            label: '10',
        },
    ];


    return (
        <div className='prompt-window'>
            <Navbar />
            <div >
                <p className='prompt-title'>Tell Us about Yourself</p>
            </div>
            <div className='row'>
                <div className='column'>
                    <p>What is your age?</p>
                    <div className={classes.root}>
                        <Slider
                            value={value1}
                            onChange={(event, newValue) => {
                                setValue1(newValue)
                                console.log(value1);
                            }}
                            defaultValue={30}
                            aria-labelledby="discrete-slider"
                            valueLabelDisplay="auto"
                            step={1}
                            marks={marks}
                            min={1}
                            max={100}                            
                            className={classes.customSlider}
                        />

                    </div>
                </div>
                <div className='column'>
                    <p>How comfortable are you with social media?</p>
                    <div className={classes.root}>
                        <Slider
                            value={value2}
                            onChange={(event, newValue) => {
                                setValue2(newValue)
                                console.log(value2);
                            }}
                            defaultValue={30}
                            aria-labelledby="discrete-slider"
                            valueLabelDisplay="auto"
                            step={1}
                            marks={marks2}
                            min={1}
                            max={10}                            
                            className={classes.customSlider}                            
                        />
                    </div>
                </div>

            </div>
            <div className='row'>
                <div className='column'>
                    <p>How comfortable are you with hardware?</p>
                    <div className={classes.root}>
                        <Slider
                            value={value3}
                            onChange={(event, newValue) => {
                                setValue3(newValue)
                                console.log(value3)
                            }}
                            defaultValue={30}
                            aria-labelledby="discrete-slider"
                            valueLabelDisplay="auto"
                            step={1}
                            marks={marks2}
                            min={1}
                            max={10}                            
                            className={classes.customSlider}                            
                        />
                    </div>
                </div>
                <div className='column'>
                    <p>Write down more information</p>
                    <input 
                        className='extra-info'
                        value={value4}
                        onChange={(event) => setValue4(event.target.value)
                        }
                        placeholder="Type here..."
                    />

                </div>
            </div>
            <center>
                <button className='info-submit' onClick={() => console.log('test')}>Submit</button>
            </center>
        </div>
    )
}

export default Prompt