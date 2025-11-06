# flake8: NOQA E501
import ast
from textwrap import dedent

from core.text import MessageStep, Page, Step, VerbatimStep, search_ast

# ...existing code...

class IntroducingTheShell(Page):
    class first_expression(VerbatimStep):
        """
右側にあるのが*シェル*です。これは小さなPythonコードを実行する場所です。コードを入力してEnterキーを押すと、すぐに実行されます。今試してみましょう：

1. シェル（黒い領域）をクリックします。
2. `__program__` と入力します。
3. キーボードの Enter キーを押します。
        """

        program = "1+2"

        class anything_else(MessageStep):
            """
            素晴らしい、自分で色々試してみているんですね！
            とても良い兆候です。その調子で続けてください。
            ただし、先に進むには最終的に `1+2` を入力する必要があることをお知らせしておきます。
            """

            program = "'literally anything'"

            def check(self):
                return True

    class more_calculation(Step):
        """
素晴らしい！Pythonは `1+2` を評価して `3` という結果を返し、シェルはその結果を表示しました。

シェルはおそらくPythonを学ぶ上で最も重要なツールです。ここではたくさん実験して、幅広く使いこなしてください。常に「もし X を実行したらどうなるだろう？」と自問し、それをすぐに試して答え合わせをしましょう。何か間違っても怖がる必要はありません — 万一間違っても悪いことは起きません。

今度はさらに計算をしてみましょう。掛け算は `*`、割り算は `/`、引き算は `-` を使います。括弧 `(`  `)` も使えます。
        """

        requirements = "シェルで `1 + 2` のような計算を実行してください。ただし `+` の代わりに `*`、`/`、または `-` を使ってください。"

        program = "5 - 6"

        class special_messages:
            class multiply_with_x:
                """
                「x」が見えますね。掛け算をしたい場合は、英字の x ではなくアスタリスク `*` を使ってください。例えば：

                    3 * 4
                """

                program = "3 x 4"

        def check(self):
            try:
                return search_ast(self.tree, (ast.Mult, ast.Div, ast.Sub))
            except SyntaxError:
                if "x" in self.input:
                    return self.special_messages.multiply_with_x

    final_text = """
いいですね！引き続き実験を続けてください。準備ができたら「次へ」をクリックして進んでください。
"""


class NavigatingShellHistory(Page):
    final_text = """
ヒント：以前入力したコードや少し修正したコードを再実行したくなることがよくあります。コピー＆ペーストでもできますが、面倒で実験の邪魔になります。より良い方法はキーボードの上矢印キー（Up Arrow）を押すことです。これで直前に入力した行がシェルに挿入されます。さらに過去に遡りたい場合は何度も押し、行き過ぎたら下矢印キー（Down Arrow）で戻れます。今試してみてください。
    """
# ...existing code...