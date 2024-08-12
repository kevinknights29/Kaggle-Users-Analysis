import mesop as me
import pandas as pd

ROOT_BOX_STYLE = me.Style(
    background="linear-gradient(to bottom, #e7f2ff, #ffffff)",
    min_height="100vh",
    font_family="Inter, sans-serif",
    display="flex",
    flex_direction="column",
    padding=me.Padding().all("2rem"),
)

TITLE_STYLE = me.Style(
    font_size="2rem",
    font_weight="bold",
    color="#1a365d",
    margin=me.Margin(bottom="2rem"),
)

SECTION_STYLE = me.Style(
    background="#ffffff",
    border_radius="8px",
    padding=me.Padding().all("1.5rem"),
    margin=me.Margin(bottom="1.5rem"),
    box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
)

BUTTON_STYLE = me.Style(
    background="#3182ce",
    color="#ffffff",
    padding=me.Padding(top="0.5rem", bottom="0.5rem", left="1rem", right="1rem"),
    border_radius="4px",
    font_weight="bold",
    cursor="pointer",
)

TABLE_STYLE = me.Style(
    width="100%",
)

TABLE_CELL_STYLE = me.Style(
    padding="0.75rem",
    border=me.Border(bottom="1px solid #e2e8f0"),
)


@me.stateclass
class State:
    clicked: bool = False
    selected_values: list[str]


def app_title():
    me.text("Kaggle Users Analysis", style=TITLE_STYLE)


def on_selection_change(e: me.SelectSelectionChangeEvent):
    s = me.state(State)
    s.selected_values = e.values


def country_selector():
    me.select(
        label="Select Country or Countries of Interest:",
        options=[
            me.SelectOption(label="Panama", value="Panama"),
        ],
        on_selection_change=on_selection_change,
        style=me.Style(
            width="100%",
            max_width="500px",
            margin=me.Margin(bottom="1rem"),
        ),
        multiple=True,
    )


def submit_button_click(event: me.ClickEvent):
    state = me.state(State)
    state.clicked = True
    me.navigate("/results")


def submit_analysis():
    me.button("Submit", on_click=submit_button_click, style=BUTTON_STYLE)


@me.page(
    path="/",
    security_policy=me.SecurityPolicy(dangerously_disable_trusted_types=True),
)
def main():
    with me.box(style=ROOT_BOX_STYLE):
        app_title()
        with me.box(style=SECTION_STYLE):
            country_selector()
        with me.box(style=SECTION_STYLE):
            submit_analysis()


df = pd.read_csv("panama_df.csv")
df["PerformanceTier"] = df["PerformanceTier"].astype(int)
df["Id"] = df["Id"].astype(int)
df = df.sort_values(
    by=[
        "PerformanceTier",
        "Id",
    ],
    ascending=[False, True],
)


def top_3_users():
    me.text(
        "Top 3 Users",
        style=me.Style(
            font_size="1.5rem",
            font_weight="bold",
            margin=me.Margin(bottom="1rem"),
        ),
    )
    with me.box(style=TABLE_STYLE):
        me.table(
            data_frame=df.head(3),
            header=me.TableHeader(sticky=True),
        )


def leaderboard():
    me.text(
        "Complete Leaderboard",
        style=me.Style(
            font_size="1.5rem",
            font_weight="bold",
            margin=me.Margin(bottom="1rem"),
        ),
    )
    with me.box(style=TABLE_STYLE):
        me.table(
            data_frame=df,
            header=me.TableHeader(sticky=True),
        )


@me.page(
    path="/results",
    security_policy=me.SecurityPolicy(dangerously_disable_trusted_types=True),
)
def results():
    with me.box(style=ROOT_BOX_STYLE):
        app_title()
        with me.box(style=SECTION_STYLE):
            top_3_users()
        with me.box(style=SECTION_STYLE):
            leaderboard()
