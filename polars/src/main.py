import altair as alt
from chart import ChartServer
from lib import run_polars


def main():
    # server = ChartServer(port=8088)
    # server.start()

    df = run_polars()

    chart = alt.Chart(
        df,
        title="Scatter plot of Age and Fare"
    ).mark_circle().encode(
        x="Age:Q",
        y="Fare:Q"
    )

    # server.open_chart(chart)

    # try:
    #     # Keep script running to keep the server alive
    #     while True:
    #         pass
    # except KeyboardInterrupt:
    #     print("\nShutting down the server...")
    #     server.stop()


if __name__ == "__main__":
    main()
