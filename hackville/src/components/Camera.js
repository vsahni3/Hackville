import React, {useRef, useEffect, useContext} from 'react'
import './Camera.css'
import CameraSubmit from './img/white_button.png'
import { Link, useNavigate } from 'react-router-dom';
import { AppContext } from './Context';
import { useSpeechRecognition, useSpeechSynthesis } from 'react-speech-kit';

const Camera = () => {
    const { photoTaken, setPhotoTaken } = useContext(AppContext);
    const videoRef = useRef(null);
    const photoRef = useRef(null);
    const snapRef = useRef(null);
    const navigate = useNavigate();
    const { speak } = useSpeechSynthesis();


    useEffect(() => {
        getVideo();
    }, [videoRef]);

    const getVideo = () => {
        navigator.mediaDevices
            .getUserMedia({ video: { width: 300 } })
            .then(stream => {
                let video = videoRef.current;
                video.srcObject = stream;
                video.play();
            })
            .catch(err => {
                console.error("error:", err);
            });
    };

    const addPhoto = () => {
        let video = videoRef.current;
        let photo = photoRef.current;
        let ctx = photo.getContext("2d");

        const width = 320;
        const height = 240;
        photo.width = width;
        photo.height = height;

        return setInterval(() => {
            ctx.drawImage(video, 0, 0, width, height);
        })
    }

    const takePhoto = () => {
        let photo = photoRef.current;
        let snap = snapRef.current;

        const data = photo.toDataURL("image/jpeg");

        console.warn(data);
        const link = document.createElement("a");
        link.href = data;
        link.setAttribute("download", "myWebcam");
        link.innerHTML = <img src='${data}' alt='thumbnail' />;
        snap.insertBefore(link, snap.firstChild);
    };

    return (
        <div className="container2">
            <div className="webcam-video">
                <video
                    onCanPlay={() => addPhoto()}
                    ref={videoRef}
                    className="player"
                />
                <canvas ref={photoRef} className="photo" />
                {/* <div className="photo-booth">
                    <div ref={snapRef} className="strip" />
                </div> */}
                <button>
                    <img 
                        src={CameraSubmit} 
                        className='photo-button' 
                        onClick={() => {
                            setPhotoTaken(true)
                            // const dummy = "We identified the technology";
                            speak({ text: "We identified the technology" })
                            navigate('/dashboard/')}
                        }/>Take a photo
                </button>

            </div>
        </div>
    );
}


export default Camera