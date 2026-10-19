from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>C Projects Store</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #f1f5f9;
                color: #172554;
            }
            header {
                background: #0b1730;
                color: white;
                padding: 24px;
                text-align: center;
            }
            header h1 {
                margin: 0;
            }
            .hero {
                background: #173d71;
                color: white;
                text-align: center;
                padding: 45px 20px;
            }
            .hero h2 {
                font-size: 32px;
            }
            .projects {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 24px;
                padding: 30px 16px;
            }
            .card {
                background: white;
                padding: 24px;
                border-radius: 14px;
                width: 300px;
                box-shadow: 0 5px 20px #00000012;
            }
            .card h3 {
                color: #1266cf;
            }
            .price {
                font-size: 23px;
                font-weight: bold;
            }
            .button {
                display: inline-block;
                background: #1976e9;
                color: white;
                text-decoration: none;
                padding: 12px 18px;
                border-radius: 7px;
                margin-top: 8px;
            }
            footer {
                background: #0b1730;
                color: white;
                text-align: center;
                padding: 20px;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>C Projects Store</h1>
            <p>Educational C Programming Projects</p>
        </header>

        <section class="hero">
            <h2>Build Your Future with C</h2>
            <p>Explore projects, learn programming and build your skills.</p>
        </section>

        <section class="projects">
            <div class="card">
                <h3>6G Network Simulator in C</h3>
                <p>An educational project demonstrating simulated
                network concepts using C.</p>
                <p>Includes source code and setup instructions.</p>
                <p class="price">$9.99</p>
                <a class="button"
                
                                href="https://asishprojects.gumroad.com/l/fiunqp"
                                target="_blank"
                                rel="noopener noreferrer">
                                Buy on Gumroad
                                </a>
            </div>

            <div class="card">
                <h3>Advanced Traffic Signal Simulator</h3>
                <p>An educational C project demonstrating traffic
                signal logic and timings.</p>
                <p>Includes source code and documentation.</p>
                <p class="price">$4.99</p>
                <a class="button"

                href="https://asishprojects.gumroad.com/l/ltqtq?wanted=true"
                target="_blank"
                rel="noopener noreferrer">
                Buy on Gumroad
                </a>
            </div>
        </section>

        <footer id="contact">
            <p>Contact: Add your business email here</p>
            <p>© 2026 C Projects Store</p>
        </footer>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)