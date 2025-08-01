export default function LoadingIndicator({theme}) {
    return <div className="loading-container">
        <h2>Generating your "{theme}" story</h2>

        <div className="loading-animation">
            <div className="spinner"></div>
        </div>

        <p className="loading-info">
            Be patient while I work hard to generate your story...
        </p>
    </div>
}