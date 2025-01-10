% rebase('layout.tpl', title=title, year=year, results=results)

<form method="get">
    <dl>
        <p>
            <dl>
                <p>
                    <h4>Введите ИНН:</h4>
                    <div>
                        <input type='text' id='inn' name='inn' placeholder='Введите ИНН' required>
                    </div>
                </p>
                <p>
                    <input type="submit" value="Поиск">
                </p>
            </dl>
        </p>
    </dl>
</form>

%if results:
<div class="px-5 mx-5">
    <h1>Результаты:</h1>

    <h4>
        <table class="table table-striped table-bordered">
            <thead>
                <tr>
                    <b>
                    <th>База данных</th>
                    <th>Результат</th>
                    </b>
                </tr>
            </thead>

            <tbody>
                %for key, val in results.items():
                <tr>
                    <td>{{key}}</td>
                    <td>{{val}}</td>
                </tr>
                %end
            </tbody>
        </table>
    </h4>
</div>
%end
