      <h1>{{ single_list[0][0] }}</h1>
        {% for task in single_list %}
          <div class="task">
            <div class="taskTop">
              <input type="text" value={{ task[1] }} />

            </div>
            <div class="taskBottom">

            </div>
          </div>
        {% endfor %} 


        # 

        
<!-- <div id="lists">
<!-- To view the lists -->
<a class="link_to_list" href="/">All Tasks</a>
{% for list in lists %}
<!-- print(f"lists/list['list_id']") -->
<a class="link_to_list" href="?list={{ list['list_id'] }}">{{list['name']}}</a>
{% endfor %}
</div> -->