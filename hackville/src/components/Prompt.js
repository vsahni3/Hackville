import React from 'react'
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
    },
    customSlider: {
        alignSelf: 'center',         
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
    const [value1, setValue1] = React.useState(30);
    const [value2, setValue2] = React.useState(30);
    const [value3, setValue3] = React.useState(30);

    // const handleChange = (event, newValue) => {
    //     setValue(newValue);
    //     console.log(value, "slider value")
    // };

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
                                    aria-labelledby="continuous-slider"
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
                            aria-labelledby="continuous-slider"
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
                            aria-labelledby="continuous-slider"
                            className={classes.customSlider}
                        />
                    </div>
                </div>
                <div className='column'>
                    <p>Write down more information</p>

                </div>

            </div>
        </div>
    )
}

export default Prompt