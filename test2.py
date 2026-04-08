import cv2
import numpy as np

def detect_gauge_precise(img_path, out_path):
    img = cv2.imread(img_path)
    if img is None:
        raise FileNotFoundError(f"图像未找到: {img_path}")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(gray, (9, 9), 2)
    edges = cv2.Canny(blurred, 30, 100)
    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1.2, minDist=150,
                               param1=50, param2=30, minRadius=100, maxRadius=250)
    if circles is None:
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if not contours:
            cv2.imwrite(out_path, img)
            return
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)
        cx = int(M["m10"] / M["m00"]) if M["m00"] != 0 else img.shape[1] // 2
        cy = int(M["m01"] / M["m00"]) if M["m00"] != 0 else img.shape[0] // 2
        r = int(cv2.contourArea(c) ** 0.5 / np.pi ** 0.5) + 15
    else:
        cx, cy, r = map(int, circles[0][0])
        r += 12

    angle_step = 1
    max_val = -1
    best_angle = 0
    search_radius = r + 20

    for deg in range(0, 360, angle_step):
        rad = np.deg2rad(deg)
        x_end = int(cx + search_radius * np.cos(rad))
        y_end = int(cy + search_radius * np.sin(rad))
        pts = []
        for t in np.linspace(0.3, 1.0, 10):
            px = int(cx + (x_end - cx) * t)
            py = int(cy + (y_end - cy) * t)
            if 0 <= px < img.shape[1] and 0 <= py < img.shape[0]:
                pts.append((px, py))
        edge_vals = [edges[py, px] for px, py in pts]
        strength = np.mean(edge_vals)
        if strength > max_val:
            max_val = strength
            best_angle = deg

    rad_best = np.deg2rad(best_angle)
    x2 = int(cx + (r + 15) * np.cos(rad_best))
    y2 = int(cy + (r + 15) * np.sin(rad_best))

    dial_angle_0_top = (best_angle + 90) % 360
    reading = (dial_angle_0_top / 360.0) * 100.0
    reading = round(reading, 1)

    vis = img.copy()
    cv2.circle(vis, (cx, cy), r, (0, 255, 255), 3)
    cv2.line(vis, (cx, cy), (x2, y2), (0, 0, 255), 3)
    text_x = int(x2 - 25) if x2 > cx else int(x2 + 10)
    text_y = int(y2 - 15)
    cv2.putText(vis, f"{reading:.1f}", (text_x, text_y),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imwrite(out_path, vis)
    print(f"读数: {reading:.1f}")

detect_gauge_precise(
    r"C:/Users/Lizhen/Desktop/test4.2/test2/yibiao1.jpeg",
    r"C:/Users/Lizhen/Desktop/test4.2/test2/yibiao1_result.jpeg"
)