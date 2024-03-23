import plotly.graph_objects as go


def plot_bezier(control_points, bezier_points):
    # Creating the plot
    fig = go.Figure(data=[
        go.Scatter3d(
            x=bezier_points[:, 0],
            y=bezier_points[:, 1],
            z=bezier_points[:, 2],
            mode='lines+markers',
            line=dict(color='blue', width=2),
            marker=dict(color='blue', size=2),
        )
    ])

    # Adding control points to the plot
    fig.add_trace(go.Scatter3d(
        x=control_points[:, 0],
        y=control_points[:, 1],
        z=control_points[:, 2],
        mode='markers+text+lines',
        line=dict(color='red', width=1),
        marker=dict(color='red', size=5),
        text=[f"P{index}" for index, _ in enumerate(control_points)],
        textposition="bottom center")
    )

    fig.update_layout(
        scene=dict(
            xaxis=dict(range=[0, 10]),  # Set x-axis limits
            yaxis=dict(range=[0, 10]),  # Set y-axis limits
            zaxis=dict(range=[0, 10])   # Set z-axis limits
        ),
        title="3D Cubic Bézier Curve",
        autosize=False,
        width=800,
        height=600,
        margin=dict(l=65, r=50, b=65, t=90)
    )
    fig.show()