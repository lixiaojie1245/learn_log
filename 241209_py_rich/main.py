from rich import print
from rich.console import Console
from rich.table import Table

print("[bold red]红色加粗[/bold red] 文本!")
print("[underline blue]蓝色下划线[/underline blue] 文本!")

console = Console()
table = Table(show_header=True, header_style="bold magenta")
table.add_column("日期", style="dim", width=12)
table.add_column("描述")
table.add_column("类型")
table.add_row("2023-02-01", "Rich 库介绍", "教育")
table.add_row("2023-02-02", "Python 教程", "编程")
console.print(table)
