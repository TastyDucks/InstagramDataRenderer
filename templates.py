CSS="""body
{
    background-color: #fafafa;
    font-family: "Montserrat-Light";
    font-size: 1em;
    margin: 1em auto;
    max-width: 40em;
    padding: 0 .62em;
}
h1, h2, h3, h4, h5, h6
{
    line-height: 1.2;
}
.conversation
{
    border-top-style: solid;
    border-top-width:0.15em;
    border-bottom-style: solid;
    border-bottom-width:0.15em;
}
.message
{
    font-family: "Montserrat-Light";
    font-size: 1em;
}
.widebody
{
    max-width: 70em;
}
.media
{
    border-style: solid;
    border-width: 0.05em;
    max-width: 50%;
}
@font-face {
    font-family: "Montserrat-Light";
    src: url("Montserrat-Light.ttf") format("truetype");
}
"""

Index = """<!DOCTYPE html>
<html>
<head>
    <title>Instagram</title>
    <link href="data:image/x-icon;base64,AAABAAIAEBAAAAEAIABoBAAAJgAAACAgAAABACAAqBAAAI4EAAAoAAAAEAAAACAAAAABACAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB00vs5fd3/coXe/9eG4P//gNr//3jS/v9sxv7/X7P9/1Wa/P9PePTYVFLtc2U54DoAAAAAAAAAAAD//wFVuPuBZMr/+m/W//9q0f//Z83+/2PI/v9cv/3/U7H8/0ic+/9AgPf/QmL0/1dN9P9tN+X7eizYhP8A/wE7lvY4Q6T8/Uiw/v9SuP3/ktb+/7bk//+75f//u+L+/7jc/v+y0f3/qMD7/4WQ9f9aRen/bS/i/3wu3f59Ldc5N4TydDaR//85l/n/w+L+/83j/v+byf3/k8P9/5C8/P+Ps/z/kqz6/6Cr+P/U1Pv/zL/2/3Ix4P9/LuP/gC/Xjj9x6dgwdvL/e6v4/8/f/f8rgPn/In/6/x50+f8lbvj/KWL3/ytS8/88SO//VD/p/9vS+f+kdun/eCfa/4Mv1/1NZuL/OmPn/6u/9/+Ztvn/J2v0/zBv9v+Iq/r/0N39/9Hb/f+Smvb/UkHr/1sp5P+2mfD/wqLv/3gm2P+GMNb/X1XT/0xT2/+4vvP/mKj0/zJV7P+Rpfb/3d77/3V78f96dvD/4d37/6SI7/9iHN7/s5Dt/8iq7/98Jtb/ii/U/3ZEv/9iQcv/wbnu/6Cd7v9LR+H/29r5/31z7P9OOOX/Vi7j/4xn6P/g0ff/bCPb/7SP6//Lq+7/gSbT/5Au0f+ON6r/fTC0/8qy5f+tk+X/YzPS/9/W9v+LaOL/ZybY/2si2P+UZOP/4dL3/3Mk1v+3j+n/zqvs/4klzv+WLs3/mziZ/44tov/Rr93/uY/b/3YhwP+1iuD/5Nn2/5dj3P+XZN7/5dv3/66B4v90G83/vJLm/9Gp6v+RJcn/nC/J/6Y7i/+YMJH/0anU/8SZ1/+GKbP/hzG//7qK2//j0fH/49Hx/7OC3f+0h+H/rnTb/8CT4f/Ro+X/mCfC/6Mxw/+sO37YpzWC/8OBtf/l0er/kzSk/48rq/+IJLH/iSq3/4kpuv+EHbn/tnXR/7N1zv/hzO7/wHjU/6Iru/+pMrn9uztydL08ev+wPn7/5cHW/+XP5//LnNL/x5PS/8WR1P/GkNb/x5HX/8aT1//hyev/477m/6k2tP+0NLj/sDSwjsRAZDjFRGb9wEBp/7tEcP/RhKH/3qnA/+Cwyv/fsM//3q/S/92s1P/ao9L/ynrC/7A3qP+0M6f/ujan/rc2oTn/AAABzlVTgdNbVvrUW1n/yVFX/8FKXf+9R2j/ukNy/7g/ev+2OoL/tTaJ/7k1kf/DOpr/wjmY+704l4T/AP8BAAAAAAAAAADXZ0g52WlKctRnStfVZ0z/0WNR/85fWv/LW2P/ylZq/8pRc//JSnjYykOFc8Y5iDoAAAAAAAAAAMADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMADAAAoAAAAIAAAAEAAAAABACAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGbM/wV92f81gd3/YYTf/36F3v/Th97/+4bf//+F3f//g9z//3/Y//971f7/d9D+/3HK/v9rw/3/ZLr9/16w/P9Yo/v/VJb5/1CG9fxPdPPVUGDvgFZO6mJdQeg3VSvVBgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABlx/9ObtH/yHPV//x73f//f+D//33c//982f7/fNn+/3vY/v951v7/dtP+/3LP/v9tyv7/aMT9/2O8/f9ds/z/V6j8/1Kc+v9Ojvj/TH71/0xu9P9RXff/WE7y/2BC5/1sN+PLcy/aUgAAAAAAAAAAAAAAAAAAAAAAAAAAVrn9dF/E/v1ly///Zsr//2rN/v9tz/7/b9H+/3DR/v9w0f7/b9D+/23O/v9qy/7/Z8b+/2PB/f9eu/3/WbP8/1Sp/P9Pnvv/S5H5/0iD9v9Hc/T/R2Lx/0xS7f9VSOn/YD7l/2815v94L+D+ey7ZegAAAAAAAAAAAAAAAEqo+ExPsv79Urj//1a8/f9awP3/XcT+/2DG/v9gx/7/Xcb+/1rE/v9Ywv7/Vr/+/1S8/v9Rt/3/TbH9/0mq/P9Fofv/QJb7/zyK+v85fPj/OW/1/zxi8/9EV/D/Tk7t/1dF6f9iO+X/bTHg/3ct3v99L9/+ey7XUwAAAABJktsHQJz2zESo//9Gq/z/SrH9/062/f9Puf3/S7f9/1q+/v99zP7/ltb+/6Ha/v+n2/7/qNr+/6jY/v+m1f7/pdH+/6PN/f+gx/3/nL/8/5Sz+/+Gofn/a4D0/01Y7/9HQuv/WEDo/2Q45P9vL+D/di3d/34w4P99LtfScTnGCTqM9TU6kvj9Opj5/zyf+v8/pfz/P6j8/0Oq/P+X0f7/5fT/////////////////////////////////////////////////////////////////////////////4+T8/5mS8/9YOub/ZTHj/3Et3/92Ld3/ey7b/4Av2/6CMNg7N4PyYTmN/f81jfb/NZL4/zSW+v83mfv/tdr+////////////4e/+/77d/v+v1f7/qNH+/6TN/f+jyv3/osf9/6HD/P+gv/z/obv7/6W6+/+uvPr/wMf6/+Tl/f///////////7+v9P9mLeH/cSvf/3ct3f97Ltv/hDDh/4Ew12U4fO2AOYT6/zSE8/8yiPb/J4T3/4y+/P//////8/j//3y1/P81kfv/K477/yuN+/8qivv/KYb6/yh/+v8nePn/JnD5/yVo+P8nYPf/LFr1/zFT8/85S/D/Sk3u/5GK8v/29v7//////6iE7f9rJN3/dy3d/3wu2/+CL93/gy/Wwzxz6dM6efD/NXvx/zB98/86hPX/5/D+//////94q/v/HHj5/ymE+v8shvr/LIX6/yyC+v8sffr/LHf5/ytx+f8tbPj/MWf3/zVj9v86XfT/QFfy/0dP8P9LRez/Ri/n/5iE7///////6+L6/3Y03/93K93/fC7b/4Av2P+GMNv/Q23m+z9w6v86dO3/L3Dw/2eX9f//////3uj+/y129/8pevj/K335/yt8+f8revn/Knb5/yRs+P8oafj/M2v3/zZn9v8wXPT/M1bz/z9W8v9GUfD/TUru/1RC6/9ZN+f/YjXj/+ni+///////kl3k/3Qn2/99Ltr/gS/Y/4Uv1v9KZuH/RWrl/0Bt6v8yZ+z/iaj1//////+3y/v/J2r0/zB19v8wdvb/MHT3/yxu9/8wbff/eZ75/7/Q/P/e5v3/3uX9/8HL+/+Ajvb/RU7v/0lG7f9UQ+v/Wzvp/2Iz5f9hJOD/zrv1//////+nfen/cyTZ/34u2f+CL9j/hjDW/1Jf2/9NYuD/R2Xl/zlf5/+arvT//////6m9+P8tY/D/Nm3z/zZt9P8xaPT/Q3L1/8TS/P/////////////////////////////////Hxvn/W0zr/1c46P9iNOb/aS3j/2Qh3v/DqvL//////7KL6/9zJNj/gC/Z/4Qv1/+HL9X/W1jV/1Zb2v9QXt//QVbi/6Sv8v//////pbX2/zRb7P89Ze//O2Tw/z1i8P/I0/v//////+3v/v+Vn/b/ZXHx/2hv8f+cm/T/8PD9///////Mw/j/XzPl/2gs4/9uK+H/ZyLd/7+j8P//////t5Lr/3Qk1v+CL9j/hjDW/4kw1P9mUM3/YFPT/1lW2P9KTtv/qq7w//////+mrvP/PVPn/0Vc6/89Vev/h5Xz///////t7v3/Y2vv/zpC6/9ERuv/SELq/0Q15/9yYOv/8e79//////+ac+v/ZyPf/3Ar3/9qItv/vqDv//////+6luv/diTV/4Qv1/+IMNX/jC7T/3FHxP9rSsr/ZE3R/1RF0/+wq+z//////6mq8P9GSeH/TVPl/0hN5v/Mzfj//////5qZ8f9BPeb/Ukfp/1ZE6P9ZQOf/XDvm/1In4f+pke7//////9G99f9qJd3/cizd/20i2v++n+7//////7uX6v95JdT/hjDW/4sv0/+QLdH/fj+4/3dBwP9wRMf/YDzK/7Wo6P//////raXs/1BA2v9WSN//Wk3h/+fl+///////cWPn/1M74v9dP+T/YDzj/2Q34v9oMuH/ZCfe/4VW4///////5935/3Mv3P91K9v/cCPY/7+f7f//////vZfq/3wl0v+KL9T/jy3S/5It0P+LN63/hDm1/307vf9tM8D/uqTk//////+zoej/XDfS/2I/2P9kRNr/6OT6//////96XOL/XjLc/2g23v9sMt7/by/d/3Et3f9qJdr/iFfh///////o3fn/dzDa/3gs2f9yI9X/wJ/s//////+/l+n/fyXQ/44t0v+SLdD/lS7O/5M2pP+PNav/ijSy/3ors//AoN7//////7md5P9pLcn/bzbP/2kx0P/VxvL//////6mM5/9hIdL/ci7Y/3Qt2f91Ldn/dCzZ/2cf1P+xkOn//////9S+8v90J9X/fC3W/3Yk0//CoOv//////8CX5/+EI83/kS3P/5Uuzv+XL8z/mDed/5Q2pP+QNar/gymq/8Se2f//////v5vf/3Umv/98MMf/dCjI/6h73f//////8ev6/4ZQ1/9pIM7/cifS/3In0v9qH9D/ilTb//Pt+///////pHTh/3cm0v+AL9T/eSXQ/8Sh6v//////w5Xl/4kjy/+ULs3/mC/L/5ovyv+dOZX/mTec/5U2o/+JKqP/xZvV///////En93/fCe4/4Mxwf+BL8T/fTHH/9rF7///////8uz6/7CM4/+NVtb/jlfX/7KO5f/z7vv//////9S/8P92Kc7/fSnP/4Mu0P98Jcz/yKTp///////DkuP/jSPI/5guyv+bL8n/nS/H/6E6jf+fOZT/mjeb/48sm//Elc7//////8qn3f+CKLH/iTK7/4cywP+CLcH/iT/H/9rD7f/////////////////////////////////Vvu7/fTTL/4tF0f+aVtb/hC3L/34jxv/Nquj//////8KM4P+RJMX/my/H/54vxv+gMMT/pjqG/6M6i/+gOZL/li6U/8CIw///////1rjg/4cqqP+OM7T/jTO5/4wzvP+GLr7/hjLA/6951v/Yv+z/6971/+vd9f/Xvu3/rHXZ/30qxf+PRs3/9Oz6//37/v+tb9f/fBq9/9i76///////vX7a/5Ymwv+fMMT/oTHC/6QxwP+rO4L7qDqE/6U6if+dMoz/tGuu///////t3+//kDaj/5Ezq/+SNLH/kTS1/480uf+NMrr/hiq6/4UsvP+KNcD/ijXC/4Urwf+FKcH/hyvC/6JZz////////////7iC1/+EJbn/7uL2//////+xX87/nCq//6MxwP+lMb7/pzG9/648fNOvPIH/qjuC/6Y4hf+lQ5D/8+jy//////+5fr7/jSeZ/5Uzp/+VNa3/lDWx/5M0tP+SM7b/kDO4/44xuv+OMbv/jzK9/5Exvv+RL77/kCy8/7Ry0P+7g9P/hSKx/7d90f//////8eP2/6I4vv+iL7z/pjK7/6gyuv+uM7z/szx2gLo+ff+wPHz/rTt//6Qyff/Mkbv///////nz+P+8f7z/mDic/5Mtnf+SLKH/kSul/5AqqP+PKav/jyit/5Anrv+RJrD/kSWw/5ElsP+PI6//iByr/4smrf+5fM7/+vX7///////Ih9T/oCm0/6gyuP+qM7b/sDS4/64zs8O7Om5hwT11/7c6dP+0O3f/sTl4/6w5e//ftc7////////////v4e7/3bzd/9Wt1//RpdX/z6LV/8+g1v/Pn9b/z5/X/8+f2P/QoNn/0aPb/9Sq3f/bu+T/7+Hz////////////2q3f/6Uwsf+pMrL/rDOy/64zsf+4Nrb/szWuZcA6ajXBPGz9vTxu/7s7cP+5O3L/tTdx/7E4df/SjrL/8+Ls////////////////////////////////////////////////////////////////////////////8eDx/8yIzf+oMav/rDGs/680rf+xNKv/szWr/7g2rP62NKk7tklJB8REYszJRmf/wUNm/8BDaP++Qmr/vEBr/7Y4af+4R3j/xWuV/8+Hq//TlLf/1Zq+/9Wcwv/VnMX/1JvH/9Sbyf/Tmsv/05nL/9KWy//Pj8n/yYDD/71itv+uO6b/qiyh/7A0pf+yNab/tDWl/7U1pf+8N6j/uTWj0qo5qgkAAAAAzU1bTM9RW/3LUFz/x05d/8ZOX//FTWH/w01i/8BKZP+8RGb/uD9p/7Y9bv+0OnP/sjl3/7A3fP+vNYH/rjOF/60xif+sL43/rC6Q/6wtk/+tLZb/ry+Z/7I0nf+1Np7/tjae/7c2nv+5N57/vDee/8E4oP67N5pTAAAAAAAAAAAAAAAA0VhRdNVcU/3VXFX/zllV/8xYVv/LWFf/yldZ/8hWW//HVGD/xVNl/8NRav/BT2//wE10/75LeP+9SXz/vEeA/7xFhP+7Qof/ukCL/7o+jv+6O5H/ujmT/7o4lf+7N5b/vTiW/8M5mf/EOZj+wDiUegAAAAAAAAAAAAAAAAAAAAAAAAAA1WJLTtllTcjWZEz922dQ/9pmUf/UY1H/0GBR/89fUv/NXlX/zFxa/8paXv/JWGP/x1Zo/8ZUbP/FUnD/xFBz/8RNd//DS3r/wkh+/8JGgf/FRIX/ykOL/8pAjf/FO4v9xjqOy8Q4jFIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAzGYzBd1qSDXaaUdh1WhIf9dqSNLVaEn71WdL/9NmTP/TZE3/0WNR/9BhVv/OX1r/zV1f/8xbY//LWGb/y1Zq/8pUbf/KUXD/yU5z+8lLd9XJSHyAy0SAYsdBgjfVK4AGAAAAAAAAAAAAAAAAAAAAAPAAAA/gAAAHwAAAA4AAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAABwAAAA+AAAAfwAAAP" rel="icon" type="image/x-icon" />
	<link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
    <h1>Index</h1>
    <ul>
        <li><a href="comments.html">💬 Comments</a></li>
        <li><a href="likedComments.html">❤️ Liked comments</a></li>
        <li><a href="likedPosts.html">💟 Liked posts</a></li>
        <li><a href="messages.html">🗫 Messages</a></li>
        <li><a href="posts.html">🖼️ Posts</a></li>
        <li><a href="profile.html">👤 Profile</a></li>
        <li><a href="savedPosts.html">💾 Saved posts</a></li>
        <li><a href="stories.html">🗞️ Stories</a></li>
        <li><a href="storyInteractions.html">📰 Story Interactions</a></li>
    </ul>
</body>
</html>"""

DirectBody = """<!DOCTYPE html>
<html>
<head>
<title>Instagram</title>
<link href="data:image/x-icon;base64,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+/+Gofn/a4D0/01Y7/9HQuv/WEDo/2Q45P9vL+D/di3d/34w4P99LtfScTnGCTqM9TU6kvj9Opj5/zyf+v8/pfz/P6j8/0Oq/P+X0f7/5fT/////////////////////////////////////////////////////////////////////////////4+T8/5mS8/9YOub/ZTHj/3Et3/92Ld3/ey7b/4Av2/6CMNg7N4PyYTmN/f81jfb/NZL4/zSW+v83mfv/tdr+////////////4e/+/77d/v+v1f7/qNH+/6TN/f+jyv3/osf9/6HD/P+gv/z/obv7/6W6+/+uvPr/wMf6/+Tl/f///////////7+v9P9mLeH/cSvf/3ct3f97Ltv/hDDh/4Ew12U4fO2AOYT6/zSE8/8yiPb/J4T3/4y+/P//////8/j//3y1/P81kfv/K477/yuN+/8qivv/KYb6/yh/+v8nePn/JnD5/yVo+P8nYPf/LFr1/zFT8/85S/D/Sk3u/5GK8v/29v7//////6iE7f9rJN3/dy3d/3wu2/+CL93/gy/Wwzxz6dM6efD/NXvx/zB98/86hPX/5/D+//////94q/v/HHj5/ymE+v8shvr/LIX6/yyC+v8sffr/LHf5/ytx+f8tbPj/MWf3/zVj9v86XfT/QFfy/0dP8P9LRez/Ri/n/5iE7///////6+L6/3Y03/93K93/fC7b/4Av2P+GMNv/Q23m+z9w6v86dO3/L3Dw/2eX9f//////3uj+/y129/8pevj/K335/yt8+f8revn/Knb5/yRs+P8oafj/M2v3/zZn9v8wXPT/M1bz/z9W8v9GUfD/TUru/1RC6/9ZN+f/YjXj/+ni+///////kl3k/3Qn2/99Ltr/gS/Y/4Uv1v9KZuH/RWrl/0Bt6v8yZ+z/iaj1//////+3y/v/J2r0/zB19v8wdvb/MHT3/yxu9/8wbff/eZ75/7/Q/P/e5v3/3uX9/8HL+/+Ajvb/RU7v/0lG7f9UQ+v/Wzvp/2Iz5f9hJOD/zrv1//////+nfen/cyTZ/34u2f+CL9j/hjDW/1Jf2/9NYuD/R2Xl/zlf5/+arvT//////6m9+P8tY/D/Nm3z/zZt9P8xaPT/Q3L1/8TS/P/////////////////////////////////Hxvn/W0zr/1c46P9iNOb/aS3j/2Qh3v/DqvL//////7KL6/9zJNj/gC/Z/4Qv1/+HL9X/W1jV/1Zb2v9QXt//QVbi/6Sv8v//////pbX2/zRb7P89Ze//O2Tw/z1i8P/I0/v//////+3v/v+Vn/b/ZXHx/2hv8f+cm/T/8PD9///////Mw/j/XzPl/2gs4/9uK+H/ZyLd/7+j8P//////t5Lr/3Qk1v+CL9j/hjDW/4kw1P9mUM3/YFPT/1lW2P9KTtv/qq7w//////+mrvP/PVPn/0Vc6/89Vev/h5Xz///////t7v3/Y2vv/zpC6/9ERuv/SELq/0Q15/9yYOv/8e79//////+ac+v/ZyPf/3Ar3/9qItv/vqDv//////+6luv/diTV/4Qv1/+IMNX/jC7T/3FHxP9rSsr/ZE3R/1RF0/+wq+z//////6mq8P9GSeH/TVPl/0hN5v/Mzfj//////5qZ8f9BPeb/Ukfp/1ZE6P9ZQOf/XDvm/1In4f+pke7//////9G99f9qJd3/cizd/20i2v++n+7//////7uX6v95JdT/hjDW/4sv0/+QLdH/fj+4/3dBwP9wRMf/YDzK/7Wo6P//////raXs/1BA2v9WSN//Wk3h/+fl+///////cWPn/1M74v9dP+T/YDzj/2Q34v9oMuH/ZCfe/4VW4///////5935/3Mv3P91K9v/cCPY/7+f7f//////vZfq/3wl0v+KL9T/jy3S/5It0P+LN63/hDm1/307vf9tM8D/uqTk//////+zoej/XDfS/2I/2P9kRNr/6OT6//////96XOL/XjLc/2g23v9sMt7/by/d/3Et3f9qJdr/iFfh///////o3fn/dzDa/3gs2f9yI9X/wJ/s//////+/l+n/fyXQ/44t0v+SLdD/lS7O/5M2pP+PNav/ijSy/3ors//AoN7//////7md5P9pLcn/bzbP/2kx0P/VxvL//////6mM5/9hIdL/ci7Y/3Qt2f91Ldn/dCzZ/2cf1P+xkOn//////9S+8v90J9X/fC3W/3Yk0//CoOv//////8CX5/+EI83/kS3P/5Uuzv+XL8z/mDed/5Q2pP+QNar/gymq/8Se2f//////v5vf/3Umv/98MMf/dCjI/6h73f//////8ev6/4ZQ1/9pIM7/cifS/3In0v9qH9D/ilTb//Pt+///////pHTh/3cm0v+AL9T/eSXQ/8Sh6v//////w5Xl/4kjy/+ULs3/mC/L/5ovyv+dOZX/mTec/5U2o/+JKqP/xZvV///////En93/fCe4/4Mxwf+BL8T/fTHH/9rF7///////8uz6/7CM4/+NVtb/jlfX/7KO5f/z7vv//////9S/8P92Kc7/fSnP/4Mu0P98Jcz/yKTp///////DkuP/jSPI/5guyv+bL8n/nS/H/6E6jf+fOZT/mjeb/48sm//Elc7//////8qn3f+CKLH/iTK7/4cywP+CLcH/iT/H/9rD7f/////////////////////////////////Vvu7/fTTL/4tF0f+aVtb/hC3L/34jxv/Nquj//////8KM4P+RJMX/my/H/54vxv+gMMT/pjqG/6M6i/+gOZL/li6U/8CIw///////1rjg/4cqqP+OM7T/jTO5/4wzvP+GLr7/hjLA/6951v/Yv+z/6971/+vd9f/Xvu3/rHXZ/30qxf+PRs3/9Oz6//37/v+tb9f/fBq9/9i76///////vX7a/5Ymwv+fMMT/oTHC/6QxwP+rO4L7qDqE/6U6if+dMoz/tGuu///////t3+//kDaj/5Ezq/+SNLH/kTS1/480uf+NMrr/hiq6/4UsvP+KNcD/ijXC/4Urwf+FKcH/hyvC/6JZz////////////7iC1/+EJbn/7uL2//////+xX87/nCq//6MxwP+lMb7/pzG9/648fNOvPIH/qjuC/6Y4hf+lQ5D/8+jy//////+5fr7/jSeZ/5Uzp/+VNa3/lDWx/5M0tP+SM7b/kDO4/44xuv+OMbv/jzK9/5Exvv+RL77/kCy8/7Ry0P+7g9P/hSKx/7d90f//////8eP2/6I4vv+iL7z/pjK7/6gyuv+uM7z/szx2gLo+ff+wPHz/rTt//6Qyff/Mkbv///////nz+P+8f7z/mDic/5Mtnf+SLKH/kSul/5AqqP+PKav/jyit/5Anrv+RJrD/kSWw/5ElsP+PI6//iByr/4smrf+5fM7/+vX7///////Ih9T/oCm0/6gyuP+qM7b/sDS4/64zs8O7Om5hwT11/7c6dP+0O3f/sTl4/6w5e//ftc7////////////v4e7/3bzd/9Wt1//RpdX/z6LV/8+g1v/Pn9b/z5/X/8+f2P/QoNn/0aPb/9Sq3f/bu+T/7+Hz////////////2q3f/6Uwsf+pMrL/rDOy/64zsf+4Nrb/szWuZcA6ajXBPGz9vTxu/7s7cP+5O3L/tTdx/7E4df/SjrL/8+Ls////////////////////////////////////////////////////////////////////////////8eDx/8yIzf+oMav/rDGs/680rf+xNKv/szWr/7g2rP62NKk7tklJB8REYszJRmf/wUNm/8BDaP++Qmr/vEBr/7Y4af+4R3j/xWuV/8+Hq//TlLf/1Zq+/9Wcwv/VnMX/1JvH/9Sbyf/Tmsv/05nL/9KWy//Pj8n/yYDD/71itv+uO6b/qiyh/7A0pf+yNab/tDWl/7U1pf+8N6j/uTWj0qo5qgkAAAAAzU1bTM9RW/3LUFz/x05d/8ZOX//FTWH/w01i/8BKZP+8RGb/uD9p/7Y9bv+0OnP/sjl3/7A3fP+vNYH/rjOF/60xif+sL43/rC6Q/6wtk/+tLZb/ry+Z/7I0nf+1Np7/tjae/7c2nv+5N57/vDee/8E4oP67N5pTAAAAAAAAAAAAAAAA0VhRdNVcU/3VXFX/zllV/8xYVv/LWFf/yldZ/8hWW//HVGD/xVNl/8NRav/BT2//wE10/75LeP+9SXz/vEeA/7xFhP+7Qof/ukCL/7o+jv+6O5H/ujmT/7o4lf+7N5b/vTiW/8M5mf/EOZj+wDiUegAAAAAAAAAAAAAAAAAAAAAAAAAA1WJLTtllTcjWZEz922dQ/9pmUf/UY1H/0GBR/89fUv/NXlX/zFxa/8paXv/JWGP/x1Zo/8ZUbP/FUnD/xFBz/8RNd//DS3r/wkh+/8JGgf/FRIX/ykOL/8pAjf/FO4v9xjqOy8Q4jFIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAzGYzBd1qSDXaaUdh1WhIf9dqSNLVaEn71WdL/9NmTP/TZE3/0WNR/9BhVv/OX1r/zV1f/8xbY//LWGb/y1Zq/8pUbf/KUXD/yU5z+8lLd9XJSHyAy0SAYsdBgjfVK4AGAAAAAAAAAAAAAAAAAAAAAPAAAA/gAAAHwAAAA4AAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAABwAAAA+AAAAfwAAAP" rel="icon" type="image/x-icon" />
<link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body class="widebody">
<h1>Messages</h1>
{Conversations}
<h1><a href="index.html">🏠 RETURN TO INDEX</a></h1>
</body>
</html>"""

ConversationBody = """<div class="conversation">
<h2>Conversation {ConversationNumber}</h2>
<p><em>{TotalMessages} messages</em></p>
<h3>Participants</h3>
<ul>
{Users}
</ul>
<h3>Content</h3>
{Messages}
</div>"""

# TODO: Change all references to "comments" in DM sections to "Messages"

DirectParticipant = """<li><strong>{Name}</strong> [{NumberOfMessages} messages, {PercentOfMessages} percent of total.]</li>"""

DirectMessage = """<div class="message">
<p>{Timestamp} | <strong>{Username}</strong></p>
<p>{Content}</p>
<p>{Likes}</p>
</div>"""

DirectMessageImage = """<div class="message">
<p>{Timestamp} | <strong>{Username}</strong></p>
<p class="media"><img width="100%" src="data:image/png;base64,{Base64Data}"></img></p>
<p>{Likes}</p>
</div>"""

DirectMessageVideo = """<div class="message">
<p>{Timestamp} | <strong>{Username}</strong></p>
<p class="media"><video controls><source type="video/mp4" src="data:video/mp4;base64,{Base64Data}"></video></p>
<p>{Likes}</p>"""

DirectMessageLikes = """️ ❤️<em> Liked by {Usernames}</em>"""